/*npm install --save-dev express cors*/
/*Per evitare di riavviare: npm i nodemon 
npx nodemon --exec node server.js*/

const express = require('express');
const cors = require('cors')

/*
const multer = require("multer");
const upload = multer({ dest: "uploads/" });
*/

const app = express();

app.use(cors());

var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"

app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//*********** 
//ROUTING
//*********** 

app.get('/formRegistrazione', (req, res) => {
console.log("Mi hai chiesto di salutarti");
//res.send("<html>Buonanotte al secchio 18 06 2024</html>");
res.sendFile("formSemplice.html", { root: './htdoc' });
});


app.get('/sendFile', (req, res) => {
    console.log("Mi hai chiesto la form di invio del file");
    res.sendFile("sendFile.html", { root: './htdoc' });
    });

//pagina di gestione dei dati della form se il metodo è POST
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.body.fname);
    response = "<html>Buona serata " + req.query.fname +" "+ req.query.fcognome;
    if(req.query.fsesso == "1")
        response += "<br>Sei un maschio"
    else
        response += "<br>Sei una femmina"
    response += "<br>Ti voglio bene"
    response += "<br>La tua città è " + req.query.fComune
    res.send(response);
    });

//GESTIONE DELLA URL MANSENDFILE
/*
app.post('/mansendfile', (req, res) => {
    
    console.log(req.body.password)
    pass_ricevuta = req.body.password;
    if(pass_ricevuta=="paperino")
        res.send("<html>Bravo " + req.body.email + "<br>Sono pronto a ricevere il file!</html>")
    else
        res.send("<html>Attenzione, password errata!!</html>")
});
*/
//app.post("/mansendfile", upload.single("file"), uploadFiles);

function uploadFiles(req, res) {
    console.log(req.body);
    console.log(req.file);
    res.send("<html>File ricevuto correttamente</html>")
}


/*
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname);
    res.send("<html>Buona serata " + req.query.fname + "</html>");
    });
*/
/*
//var mylist = "[{\"id\": 1,\"item\": \"panino con la mortadella\"},{\"id\": 2,\"item\": \"baguette\"}]";
var mylist="";

app.use('/list', (req, res) => {
console.log("Mi hai chiesto la lista del pane");	
//Leggi il file lista_panini.json e memorizza il contenuto in mylist
res.send(mylist);
});


app.use('/salutami', (req, res) => {
console.log("Mi hai chiesto di salutarti");
res.send("<html>Ciao a tutti okokok</html>");
});
*/                            