/**
 * scan-docs.js
 *
 * Script de scan de la documentation existante pour le Docs Auto-Updater.
 *
 * Usage : node scan-docs.js [workspacePath]
 */

const fs = require('fs');
const path = require('path');

const workspace = path.resolve(process.argv[2] || '.');

function listDir(dir, pattern) {
  if (!fs.existsSync(dir)) return [];
  try {
    return fs.readdirSync(dir, { withFileTypes: true })
      .filter(d => d.isFile() && d.name.endsWith(pattern))
      .map(d => d.name);
  } catch { return []; }
}

function safeRead(file) {
  try { return fs.readFileSync(file, 'utf-8'); } catch { return null; }
}

const windsurfDir = path.join(workspace, '.devin');
const skillsDir = path.join(windsurfDir, 'skills');
const rulesDir = path.join(windsurfDir, 'rules');
const workflowsDir = path.join(windsurfDir, 'workflows');

const skills = fs.existsSync(skillsDir)
  ? fs.readdirSync(skillsDir, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name)
  : [];

const rules = listDir(rulesDir, '.md');
const workflows = listDir(workflowsDir, '.md');

const readme = safeRead(path.join(workspace, 'README.md'));
const agents = safeRead(path.join(workspace, 'AGENTS.md'));
const toolsGuide = safeRead(path.join(workspace, 'TOOLS_USERGUIDE.md'));

const report = {
  scanned_at: new Date().toISOString(),
  workspace,
  windsurf: {
    skills: skills.map(s => ({
      name: s,
      has_skill_md: fs.existsSync(path.join(skillsDir, s, 'SKILL.md')),
      has_docs: fs.existsSync(path.join(skillsDir, s, 'docs', 'README.md'))
    })),
    rules: rules.map(r => ({ name: r.replace('.md', '') })),
    workflows: workflows.map(w => ({ name: w.replace('.md', '') }))
  },
  project_docs: {
    has_readme: !!readme,
    has_agents_md: !!agents,
    has_tools_guide: !!toolsGuide,
    readme_length: readme ? readme.length : 0,
    agents_length: agents ? agents.length : 0,
    tools_guide_length: toolsGuide ? toolsGuide.length : 0
  },
  coverage: {
    skills_with_docs: skills.filter(s => fs.existsSync(path.join(skillsDir, s, 'docs', 'README.md'))).length,
    total_skills: skills.length,
    coverage_percent: skills.length ? Math.round((skills.filter(s => fs.existsSync(path.join(skillsDir, s, 'docs', 'README.md'))).length / skills.length) * 100) : 0
  }
};

const outputPath = path.join(workspace, '.devin', 'skills', 'docs-auto-updater', 'data', 'last-scan.json');
fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, JSON.stringify(report, null, 2), 'utf-8');

console.log('SCAN_COMPLETE');
console.log(JSON.stringify(report, null, 2));
