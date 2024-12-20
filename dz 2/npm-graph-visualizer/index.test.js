const { getDependencies, generateGraphvizCode, main } = require('./index');

test('getDependencies should return dependencies', () => {
  const dependencies = getDependencies('express', 1);
  expect(dependencies).toHaveProperty('accepts');
  expect(dependencies).toHaveProperty('array-flatten');
});

test('generateGraphvizCode should generate valid Graphviz code', () => {
  const dependencies = {
    'dep1': {},
    'dep2': {
      'dep3': {}
    }
  };
  const graphvizCode = generateGraphvizCode(dependencies, 'root');
  expect(graphvizCode).toContain('"root" -> "dep1"');
  expect(graphvizCode).toContain('"root" -> "dep2"');
  expect(graphvizCode).toContain('"dep2" -> "dep3"');
});

test('main should write Graphviz code to file', () => {
  const fs = require('fs');
  const path = require('path');
  const outputFilePath = path.join(__dirname, 'test-output.dot');
  main(['graphviz', 'express', outputFilePath, '1']);
  const graphvizCode = fs.readFileSync(outputFilePath, 'utf-8');
  expect(graphvizCode).toContain('"express" -> "accepts"');
  expect(graphvizCode).toContain('"express" -> "array-flatten"');
  fs.unlinkSync(outputFilePath);
});
