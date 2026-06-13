/**
 * scan-workspace.js
 *
 * Script d'extraction des données brutes du workspace pour le
 * Project Context Analyzer.
 *
 * Usage : node scan-workspace.js [workspacePath] [outputJsonPath]
 * Dépendances : Node.js 18+ (modules fs, path, child_process)
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const DEFAULT_WORKSPACE = '.';
const DEFAULT_OUTPUT = '.devin/skills/premium-project-generator/data/context-report.json';

const args = process.argv.slice(2);
const workspacePath = path.resolve(args[0] || DEFAULT_WORKSPACE);
const outputPath = path.resolve(args[1] || DEFAULT_OUTPUT);

/**
 * Liste les fichiers à la racine (1 niveau)
 */
function listRootFiles(dir) {
  try {
    return fs.readdirSync(dir, { withFileTypes: true })
      .map(d => ({
        name: d.name,
        isDirectory: d.isDirectory()
      }));
  } catch {
    return [];
  }
}

/**
 * Liste récursive d'un sous-dossier (limitée en profondeur)
 */
function listSubdir(dir, maxDepth = 2, currentDepth = 0) {
  if (currentDepth > maxDepth) return [];
  try {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    let result = [];
    for (const entry of entries) {
      if (entry.isDirectory()) {
        result.push({ name: entry.name, path: path.relative(workspacePath, path.join(dir, entry.name)), type: 'dir' });
        if (currentDepth < maxDepth) {
          result = result.concat(listSubdir(path.join(dir, entry.name), maxDepth, currentDepth + 1));
        }
      } else {
        result.push({ name: entry.name, path: path.relative(workspacePath, path.join(dir, entry.name)), type: 'file' });
      }
    }
    return result;
  } catch {
    return [];
  }
}

/**
 * Lit un fichier texte de manière sécurisée
 */
function safeReadFile(filePath, maxChars = 50000) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    return content.slice(0, maxChars);
  } catch {
    return null;
  }
}

/**
 * Détecte le manifeste principal selon les fichiers présents
 */
function detectManifest(rootFiles) {
  const priority = ['package.json', 'Cargo.toml', 'pyproject.toml', 'setup.py', 'composer.json', 'go.mod', 'pom.xml', 'build.gradle', 'Gemfile'];
  for (const name of priority) {
    if (rootFiles.some(f => f.name === name && !f.isDirectory)) {
      return name;
    }
  }
  return null;
}

/**
 * Compte les contributeurs git uniques
 */
function getGitContributors(dir) {
  try {
    const stdout = execSync('git shortlog -sne HEAD 2>nul || true', { cwd: dir, encoding: 'utf-8', timeout: 5000 });
    const lines = stdout.trim().split('\n').filter(l => l.trim());
    return lines.map(line => {
      const match = line.match(/^\s*(\d+)\s+(.+)$/);
      return match ? { commits: parseInt(match[1], 10), name: match[2].trim() } : null;
    }).filter(Boolean);
  } catch {
    return [];
  }
}

/**
 * Compte les fichiers par extension dans le projet
 */
function getFileExtensionStats(dir, maxFiles = 1000) {
  const stats = {};
  let count = 0;

  function walk(current) {
    if (count > maxFiles) return;
    try {
      const entries = fs.readdirSync(current, { withFileTypes: true });
      for (const entry of entries) {
        if (entry.name.startsWith('.')) continue;
        if (entry.name === 'node_modules') continue;
        const full = path.join(current, entry.name);
        if (entry.isDirectory()) {
          walk(full);
        } else {
          count++;
          const ext = path.extname(entry.name).toLowerCase();
          if (ext) {
            stats[ext] = (stats[ext] || 0) + 1;
          }
        }
      }
    } catch {
      // ignore
    }
  }

  walk(dir);
  return stats;
}

/**
 * Analyse l'existant Windsurf
 */
function analyzeWindsurf(dir) {
  const windsurfDir = path.join(dir, '.devin');
  if (!fs.existsSync(windsurfDir)) {
    return {
      exists: false,
      rules_count: 0,
      skills_count: 0,
      workflows_count: 0,
      has_rag: false,
      has_mcp: false
    };
  }

  const rulesDir = path.join(windsurfDir, 'rules');
  const skillsDir = path.join(windsurfDir, 'skills');
  const workflowsDir = path.join(windsurfDir, 'workflows');
  const ragDir = path.join(windsurfDir, 'rag');
  const mcpDir = path.join(windsurfDir, 'integrations', 'mcp');

  const countFiles = (d) => {
    if (!fs.existsSync(d)) return 0;
    try {
      return fs.readdirSync(d, { withFileTypes: true }).filter(f => f.isFile() && f.name.endsWith('.md')).length;
    } catch { return 0; }
  };

  const countDirs = (d) => {
    if (!fs.existsSync(d)) return 0;
    try {
      return fs.readdirSync(d, { withFileTypes: true }).filter(f => f.isDirectory()).length;
    } catch { return 0; }
  };

  return {
    exists: true,
    rules_count: countFiles(rulesDir),
    skills_count: countDirs(skillsDir),
    workflows_count: countFiles(workflowsDir),
    has_rag: fs.existsSync(ragDir),
    has_mcp: fs.existsSync(mcpDir)
  };
}

// =============================================================================
// EXÉCUTION PRINCIPALE
// =============================================================================

const rootFiles = listRootFiles(workspacePath);
const manifestFile = detectManifest(rootFiles);

const rawData = {
  scanned_at: new Date().toISOString(),
  workspace_path: workspacePath,
  root_entries: rootFiles,
  manifest_file: manifestFile,
  manifest_content: manifestFile ? safeReadFile(path.join(workspacePath, manifestFile), 30000) : null,
  readme_content: safeReadFile(path.join(workspacePath, 'README.md'), 30000)
    || safeReadFile(path.join(workspacePath, 'readme.md'), 30000),
  windsurf_analysis: analyzeWindsurf(workspacePath),
  git_contributors: getGitContributors(workspacePath),
  file_extensions: getFileExtensionStats(workspacePath),
  src_structure: fs.existsSync(path.join(workspacePath, 'src'))
    ? listSubdir(path.join(workspacePath, 'src'), 2)
    : null,
  app_structure: fs.existsSync(path.join(workspacePath, 'app'))
    ? listSubdir(path.join(workspacePath, 'app'), 2)
    : null
};

// Écriture du fichier de données brutes
// Le LLM (Cascade) utilisera ce fichier + le discovery-prompt pour produire le rapport final
const rawOutputPath = outputPath.replace(/context-report\.json$/, 'context-raw.json');

fs.mkdirSync(path.dirname(rawOutputPath), { recursive: true });
fs.writeFileSync(rawOutputPath, JSON.stringify(rawData, null, 2), 'utf-8');

// Si on a les clés déjà (pas de LLM), on peut produire un rapport basique
// Mais le vrai rapport context-report.json sera produit par le LLM via le skill
console.log('SCAN_COMPLETE');
console.log(JSON.stringify({
  raw_data_path: rawOutputPath,
  files_scanned: rootFiles.length,
  manifest_detected: !!manifestFile,
  readme_detected: !!rawData.readme_content,
  windsurf_exists: rawData.devin_analysis.exists,
  git_contributors: rawData.git_contributors.length,
  top_extensions: Object.entries(rawData.file_extensions)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
}, null, 2));
