const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function getDependencies(packageName, depth, visited = new Set()) {
  if (depth === 0 || visited.has(packageName)) {
    return {};
  }
  visited.add(packageName);

  const packageInfo = JSON.parse(execSync(`npm view ${packageName} --json`));
  const dependencies = packageInfo.dependencies || {};

  const result = {};
  for (const dep in dependencies) {
    result[dep] = getDependencies(dep, depth - 1, visited);
  }
  return result;
}

function generateGraphvizCode(dependencies, packageName) {
  let graphvizCode = `digraph G {\n`;
  graphvizCode += `  "${packageName}";\n`;

  function traverse(deps, parent) {
    for (const dep in deps) {
      graphvizCode += `  "${parent}" -> "${dep}";\n`;
      traverse(deps[dep], dep);
    }
  }

  traverse(dependencies, packageName);
  graphvizCode += `}\n`;
  return graphvizCode;
}

function main(args) {
  const [graphvizPath, packageName, outputFilePath, maxDepth] = args;
  const dependencies = getDependencies(packageName, parseInt(maxDepth));
  const graphvizCode = generateGraphvizCode(dependencies, packageName);

  fs.writeFileSync(outputFilePath, graphvizCode);
  console.log(`Graphviz code written to ${outputFilePath}`);
}

if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length < 4) {
    console.error('Usage: node index.js <graphvizPath> <packageName> <outputFilePath> <maxDepth>');
    process.exit(1);
  }
  main(args);
}

module.exports = { getDependencies, generateGraphvizCode, main };
