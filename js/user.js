const mysql = require('mysql');

const connection = mysql.createConnection({
  host: '127.0.0.1',
  port: 3306,
  user: 'userN',
  password: '1234',
  database: 'flight_game',
  autocommit: true,
});

let username;

connection.connect(function(err) {
  if (err) throw err;
  const sql = 'SELECT * FROM game WHERE screen_name =' + username
  connection.query(sql, function(err, result) {
    if (err) throw err;
    console.log(result);
  });
});

