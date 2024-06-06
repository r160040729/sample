// server.js
const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');
const app = express();
const port = 5000;

const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req, res) => {
  const file = req.file;

  // Call a Python script to process the file
  const python = spawn('python', ['process_pdf.py', file.path]);

  python.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    res.send('File processed successfully');
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
