const prompt = require('prompt-sync')();

var vocali = "aeiou"
var numeri = "0123456789"

do {
    
    var parola = prompt("Scrivi una parola: ")
    var num_voc = 0
    var num_num = 0
    var num_con = 0

    for(i=0;i<parola.length;i++){

        if(vocali.includes(parola[i])){

            num_voc += 1

        }else if(numeri.includes(parola[i])){

            num_num += 1

        }else{

            num_con += 1
        }        
    }

    console.log("La parola " + parola + "è composta da " + num_voc + " vocali, " + num_con + " consonanti e " + num_num + " numeri")

    var uscita = prompt("Se vuoi uscire scrivi 'exit': ") 

}while (uscita != "exit");