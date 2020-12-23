const express    = require('express');
const mysql      = require('mysql');
const dbconfig   = require('./config/database.js');
const dbconfig_slave = require('./config/database-slave.js');
const connection = mysql.createConnection(dbconfig);
const connection_slave = mysql.createConnection(dbconfig_slave);
const bodyParser = require('body-parser')

const app = express();
app.set('port', process.env.PORT || 8000);
app.use(bodyParser.urlencoded({ extended: false }));

var res_state='complete';
  
app.get('/Customer/select', (req, res) => {
    connection_slave.query('SELECT * from Customer', (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.send(rows);
    });
});

app.post('/Customer/select/name', (req, res) => {
    console.log(req.body);
    var cust_name = req.body.cust_name;

    var sql = 'select * from Customer where cust_name=?';
    connection_slave.query(sql, [cust_name]);
    res.send(res_state);
});
  
app.post('/Customer/select/id', (req, res) => {
    console.log(req.body);
    var cust_id = req.body.cust_id;

    var sql = 'select * from Customer where cust_id=?';
    connection_slave.query(sql, [cust_id]);
    res.send(res_state);
});

app.post('/Customer/select/phone', (req, res) => {
    console.log(req.body);
    var cust_phone = req.body.cust_phone;

    var sql = 'select cust_phone from Customer where cust_phone=?';
    connection_slave.query(sql, [cust_phone]);
    res.send(res_state);
});

app.post('/Customer/insert', (req, res) => {
    console.log(req.body);
    var cust_name = req.body.cust_name;
    var cust_phone = req.body.cust_phone;
    var cust_birth = req.body.cust_birth;

    var sql = 'insert into Customer(cust_name,cust_phone,cust_birth) values(?,?,?)';
    connection.query(sql, [cust_name,cust_phone,cust_birth]);
    res.send(res_state);
});
  
app.post('/Customer/update', (req, res) => {
    console.log(req.body);
    var cust_name = req.body.cust_name;
    var cust_phone = req.body.cust_phone;
    var cust_birth = req.body.cust_birth;
    var cust_id = req.body.cust_id;

    var sql = 'update Customer set cust_name=?, cust_phone=?, cust_birth=? where cust_id=?';
    connection.query(sql, [cust_name, cust_phone, cust_birth,cust_id]);
    res.send(res_state);
});
  
  
app.delete('/Customer/delete', (req, res) => {
    console.log(req.body);
    var cust_id = req.body.cust_id;

    var sql = 'delete from Customer where cust_id=?';
    connection.query(sql, [cust_id]);
    res.send(res_state);
});

app.get('/Car/select', (req, res) => {
    connection_slave.query('SELECT * from Car', (error, rows) => {
    if (error) throw error;
    console.log('Car info is: ', rows);
    res.send(rows);
    });
  });
  
  app.post('/Car/select/id', (req, res) => {
    console.log(req.body);
    var car_id = req.body.car_id;
  
    var sql = 'select * from Car where car_id=?';
    connection_slave.query(sql, [car_id], (error, rows) => {
        console.log(rows);
        res.send(rows);
    });
  });
  
  app.post('/Car/select/name', (req, res) => {
    console.log(req.body);
    var car_name = req.body.car_name;
  
    var sql = 'select * from Car where car_name=?';
    connection_slave.query(sql, [car_name], (error, rows) => {
        res.send(rows);
    });
  });
  
  app.post('/Car/insert', (req, res) => {
    console.log(req.body);
    var car_name = req.body.car_name;
    var color = req.body.color;
    var made_by = req.body.made_by;
  
    var sql = 'insert into Car(car_name, color, made_by) values(?,?,?)';
    connection.query(sql, [car_name, color, made_by]);
    res.send(res_state);
  });

  app.post('/Car/update', (req, res) => {
    console.log(req.body);
    var car_name = req.body.car_name;
    var color = req.body.color;
    var made_by = req.body.made_by;
    var car_id = req.body.car_id;
  
    var sql = "update Car set car_name=?, color=?, made_by=? where car_id=?";
    connection.query(sql,  [car_name, color, made_by, car_id]);
    res.send(res_state);
  });
  
  app.post('/Car/update/sales', (req, res) => {
    console.log(req.body);
  
    var car_id = req.body.car_id;
  
    var sql = "update Car set sales='sold_out' where car_id=?";
    connection.query(sql,  [car_id]);
    res.send(res_state);
  });
  
  app.post('/Car/update_id', (req, res) => {
    console.log(req.body);
    var car_id = req.body.car_id;
  
    var sql = "update Car set sales='sold_out' where car_id=?";
    connection.query(sql, [car_id]);
    res.send(res_state);
  });
  
  app.delete('/Car/delete', (req, res) => {
    console.log(req.body);
    var car_id = req.body.car_id;
  
    var sql = 'delete from Car where car_id=?';
    connection.query(sql, [car_id]);
    res.send(res_state);
  });
  

app.get('/Sales_invoice/select', (req, res) => {
    connection_slave.query('SELECT * from Sales_invoice', (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.send(rows);
    });
});

app.post('/Sales_invoice/select/id', (req, res) => {
    console.log(req.body);
    var car_id = req.body.car_id;
    var cust_id = req.body.cust_id;

    var sql = 'select * from Sales_invoice where car_id =? and cust_id=?';
    connection_slave.query(sql, [car_id, cust_id], (error, rows) => {
        console.log(rows);
        res.send(rows);
    });
});
  
app.post('/Sales_invoice/insert', (req, res) => {
    console.log(req.body);
    var cust_id = req.body.cust_id;
    var sales_id = req.body.sales_id;
    var car_id = req.body.car_id;

    var sql = 'insert into Sales_invoice(cust_id,sales_id,car_id) values(?,?,?)';
    connection.query(sql, [cust_id,sales_id,car_id]);
    res.send(res_state);
});

app.get('/mechanics/select', (req, res) => {
    connection_slave.query('SELECT * from mechanics', (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.send(rows);
    });
});

app.post('/mechanics/select/name', (req, res) => {
    console.log(req.body);
    var day = req.body.day;
    var mechanic_name = req.body.mechanic_name;

    var sql = 'SELECT ? FROM mechanics where mechanic_name=?';
    if(day=='FRI'){
        var sql = "SELECT FRI FROM mechanics where mechanic_name=?";
        connection_slave.query(sql, [mechanic_name], (error, rows) => {
            res.send(rows);
        });
    }
    else if(day=='MON'){
        var sql = "SELECT MON FROM mechanics where mechanic_name=?";
        connection_slave.query(sql, [mechanic_name], (error, rows) => {
            res.send(rows);
        });
    }
    else if(day=='TUE'){
        var sql = "SELECT TUE FROM mechanics where mechanic_name=?";
        connection_slave.query(sql, [mechanic_name], (error, rows) => {
            res.send(rows);
        });
    }
    else if(day=='WED'){
        var sql = "SELECT WED FROM mechanics where mechanic_name=?";
        connection_slave.query(sql, [mechanic_name], (error, rows) => {
            res.send(rows);
        });
    }
    else if(day=='THU'){
        var sql = "SELECT THU FROM mechanics where mechanic_name=?";
        connection_slave.query(sql, [mechanic_name], (error, rows) => {
            res.send(rows);
        });
    }
});

app.post('/mechanics/update', (req, res) => {
    console.log(req.body);
    var day = req.body.day;
    var mechanic_name = req.body.mechanic_name;

    if(day=='MON'){
        var sql = "UPDATE mechanics SET MON = 'reserved' where mechanic_name=?";
        connection.query(sql, [mechanic_name]);
    }
    else if(day=='TUE'){
        var sql = "UPDATE mechanics SET TUE = 'reserved' where mechanic_name=?";
        connection.query(sql, [mechanic_name]);
    }
    else if(day=='WED'){
        var sql = "UPDATE mechanics SET WED = 'reserved' where mechanic_name=?";
        connection.query(sql, [mechanic_name]);
    }
    else if(day=='THU'){
        var sql = "UPDATE mechanics SET THU = 'reserved' where mechanic_name=?";
        connection.query(sql, [mechanic_name]);
    }
    else if(day=='FRI'){
        var sql = "UPDATE mechanics SET FRI = 'reserved' where mechanic_name=?";
        connection.query(sql, [mechanic_name]);
    }
    connection.query(sql, [day, mechanic_name]);
    res.send(res_state);;
});


app.listen(app.get('port'), () => {
    console.log('Express server listening on port ' + app.get('port'));
});