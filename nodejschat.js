const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const port = 3000;
 
// Serve static files from the public directory
app.use(express.static('public'));

// Map socket IDs to usernames
const users = new Map();

// Listen for connections
io.on('connection', (socket) => {
  let username;

  // Handle login event
  socket.on('login', (data) => {
    const { username: inputUsername, password } = data;
    if (password !== 'nss') {
      socket.emit('loginError', 'Incorrect password');
      console.log(`LOGIN ATTEMPT User: ${inputUsername}  Pass: ${password}`)
    } else {
      console.log(`User '${inputUsername}' logged in`);
      username = inputUsername;
      // Associate username with socket ID
      users.set(socket.id, username);
      socket.emit('loginSuccess');
    }
  });

  // Handle send message event
  socket.on('sendMessage', (message) => {
    // Get username from session ID
    const username = users.get(socket.id);
    console.log(`${username}: ${message}`);
    io.emit('message', { username, text: message });
  });

  // Handle disconnect event
  socket.on('disconnect', () => {
    if (username) {
      console.log(`Disconnected '${username}'`)
      // Remove username from map
      users.delete(socket.id);
    }
  });
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Start the server
http.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
  console.log("Logs:")
});
