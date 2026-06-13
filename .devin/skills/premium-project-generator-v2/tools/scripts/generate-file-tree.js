/**
 * generate-file-tree.js
 * Génère l'arborescence complète d'un projet avec outils Windsurf V2
 */

const fs = require('fs');
const path = require('path');

const WINDSURF_STRUCTURE = {
  '.devin': {
    'rules': {},
    'skills': {},
    'workflows': {},
    'rag': {},
    'integrations': {
      'mcp': {}
    }
  },
  'AGENTS.md': null,
  'TOOLS_USERGUIDE.md': null
};

function createDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
    console.log(`Created: ${dirPath}`);
  }
}

function createFile(filePath, content = '') {
  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, content);
    console.log(`Created: ${filePath}`);
  }
}

function generateStructure(basePath, structure) {
  for (const [name, content] of Object.entries(structure)) {
    const fullPath = path.join(basePath, name);
    if (content === null) {
      createFile(fullPath, `# ${name}\n`);
    } else if (typeof content === 'object') {
      createDir(fullPath);
      if (Object.keys(content).length > 0) {
        generateStructure(fullPath, content);
      }
    }
  }
}

// CLI
const targetDir = process.argv[2] || '.';
console.log(`Generating Windsurf V2 structure in: ${targetDir}`);
generateStructure(targetDir, WINDSURF_STRUCTURE);
console.log('Done!');
