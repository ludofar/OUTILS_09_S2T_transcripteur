/**
 * validate-frontmatter.js
 * Valide les frontmatter YAML des fichiers Windsurf
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
    if (!fm.name) errors.push('Missing "name"');
    if (!fm.description) errors.push('Missing "description"');
    if (!fm.trigger || !VALID_TRIGGERS.includes(fm.trigger.split(':')[0].trim())) {
      errors.push(`Invalid trigger. Must be one of: ${VALID_TRIGGERS.join(', ')}`);
    }
    if (content.length > 12000) errors.push('Content exceeds 12k characters');
    return { valid: errors.length === 0, errors };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`] };
  }
}

function validateSkill(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { valid: false, errors: ['No frontmatter found'] };

  try {
    const fm = yaml.parse(match[1]);
    const errors = [];
    if (!fm.name) errors.push('Missing "name"');
    if (!fm.description) errors.push('Missing "description" - crucial for auto-invocation');
    if (!fm.version) errors.push('Missing "version"');
    if (fm.scope && !VALID_SCOPES.includes(fm.scope)) {
      errors.push(`Invalid scope. Must be one of: ${VALID_SCOPES.join(', ')}`);
    }
    return { valid: errors.length === 0, errors };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`] };
  }
}

function validateWorkflow(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { valid: false, errors: ['No frontmatter found'] };

  try {
    const fm = yaml.parse(match[1]);
    const errors = [];
    if (!fm.description) errors.push('Missing "description"');
    return { valid: errors.length === 0, errors };
  } catch (e) {
    return { valid: false, errors: [`YAML parse error: ${e.message}`] };
  }
}

// CLI
const target = process.argv[2];
if (!target) {
  console.error('Usage: node validate-frontmatter.js <file-or-directory>');
  process.exit(1);
}

const stats = fs.statSync(target);
if (stats.isFile()) {
  const ext = path.extname(target);
  let result;
  if (target.includes('/rules/')) result = validateRule(target);
  else if (target.includes('/skills/')) result = validateSkill(target);
  else if (target.includes('/workflows/')) result = validateWorkflow(target);
  else {
    console.log('Unknown file type, trying all validators...');
    result = validateRule(target);
  }
  console.log(JSON.stringify(result, null, 2));
} else {
  console.log('Directory validation not yet implemented');
}
