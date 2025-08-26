const express = require('express');
const app = express();
const PORT = 3000;

// Home route
app.get('/', (req, res) => {
  res.send(`
    <h2>Welcome!</h2>
    <p>Use the URL format: <code>/user/yourname/yourage</code></p>
    <p>Example: <a href="/user/Akash/20">/user/Akash/20</a></p>
  `);
});

// Route with two dynamic parameters: name and age
app.get('/user/:name/:age', (req, res) => {
  const name = req.params.name;
  const age = req.params.age;

  res.send(`
    <html>
      <head>
        <title>Welcome Page</title>
        <style>
          body { font-family: Arial; background: #f2f2f2; padding: 20px; }
          h1 { color: #333; }
        </style>
      </head>
      <body>
        <h1>Hello, ${name}!</h1>
        <p>You are ${age} years old.</p>
        <p>Thanks for visiting our dynamic server 😊</p>
      </body>
    </html>
  `);
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server is running at http://localhost:${PORT}`);
});
