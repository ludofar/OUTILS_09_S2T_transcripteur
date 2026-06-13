/**
 * validate-frontmatter.js
 * Valide les frontmatter YAML des fichiers Windsurf (V2 avec staleness metadata)
 */

const fs = require('fs');
const path = require('path');
const yaml = require('yaml');

const VALID_TRIGGERS = ['always_on', 'glob', 'model_decision', 'manual'];
const VALID_SCOPES = ['workspace', 'global', 'system'];
const VALID_PRIORITIES = ['high', 'medium', 'low'];

function validateRule(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { valid: false, errors: ['No frontmatter found'] };

  try {
    const fm = yaml.parse(match[1]);
    const errors = [];
    const warnings = [];
    if (!fm.name) errors.push('Missing "name"');
    if (!fm.description) errors.push('Missing "description"');
    if (!fm.trigger || !VALID_TRIGGERS.includes(fm.trigger.split(':')[0].trim())) {
      errors.push(`Invalid trigger. Must be one of: ${VALID_TRIGGERS.join(', ')}`);
    }
    if (content.length > 12000) errors.push('Content exceeds 12k characters');

    // V2: staleness metadata
    if (!fm.metadata || !fm.metadata.created) {
      warnings.push('Missing metadata.created (V2 staleness)');
    }
    if (!fm.metadata || !fm.metadata.last_reviewed) {
      warnings.push('Missing metadata.last_reviewed (V2 staleness)');
    }
    if (!fm.metadata || !fm.metadata.review_interval_days) {
      warnings.push('Missing metadata.review_interval_days (V2 staleness)');
    }

    return { valid: errors.length === 0, errors, warnings };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`], warnings: [] };
  }
}

function validateSkill(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { valid: false, errors: ['No frontmatter found'] };

  try {
    const fm = yaml.parse(match[1]);
    const errors = [];
    const warnings = [];
    if (!fm.name) errors.push('Missing "name"');
    if (!fm.description) errors.push('Missing "description" - crucial for auto-invocation');
    if (!fm.version) errors.push('Missing "version"');
    if (fm.scope && !VALID_SCOPES.includes(fm.scope)) {
      errors.push(`Invalid scope. Must be one of: ${VALID_SCOPES.join(', ')}`);
    }

    // V2: staleness metadata
    if (!fm.metadata || !fm.metadata.created) {
      warnings.push('Missing metadata.created (V2 staleness)');
    }
    if (!fm.metadata || !fm.metadata.last_reviewed) {
      warnings.push('Missing metadata.last_reviewed (V2 staleness)');
    }

    return { valid: errors.length === 0, errors, warnings };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`], warnings: [] };
  }
}

function validateWorkflow(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { valid: false, errors: ['No frontmatter found'] };

  try {
    const fm = yaml.parse(match[1]);
    const errors = [];
    const warnings = [];
    if (!fm.description) errors.push('Missing "description"');

    // V2: staleness metadata
    if (!fm.metadata || !fm.metadata.created) {
      warnings.push('Missing metadata.created (V2 staleness)');
    }

    return { valid: errors.length === 0, errors, warnings };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`], warnings: [] };
  }
}

function validateDirectory(dirPath) {
  const results = { total: 0, valid: 0, invalid: 0, files: [] };

  function walk(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.name.endsWith('.md')) {
        let result;
        if (fullPath.includes('/rules/') || fullPath.includes('\\rules\\')) {
          result = validateRule(fullPath);
        } else if (fullPath.includes('SKILL.md')) {
          result = validateSkill(fullPath);
        } else if (fullPath.includes('/workflows/') || fullPath.includes('\\workflows\\')) {
          result = validateWorkflow(fullPath);
        } else {
          continue;
        }
        results.total++;
        if (result.valid) results.valid++;
        else results.invalid++;
        results.files.push({ path: fullPath, ...result });
      }
    }
  }

  walk(dirPath);
  return results;
}

// CLI
const target = process.argv[2];
if (!target) {
  console.error('Usage: node validate-frontmatter.js <file-or-directory>');
  process.exit(1);
}

const stats = fs.statSync(target);
if (stats.isFile()) {
  let result;
  if (target.includes('/rules/') || target.includes('\\rules\\')) result = validateRule(target);
  else if (target.includes('SKILL.md')) result = validateSkill(target);
  else if (target.includes('/workflows/') || target.includes('\\workflows\\')) result = validateWorkflow(target);
  else {
    console.log('Unknown file type, trying rule validator...');
    result = validateRule(target);
  }
  console.log(JSON.stringify(result, null, 2));
  process.exit(result.valid ? 0 : 1);
} else if (stats.isDirectory()) {
  const results = validateDirectory(target);
  console.log(JSON.stringify(results, null, 2));
  process.exit(results.invalid > 0 ? 1 : 0);
}
