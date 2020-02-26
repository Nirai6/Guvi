
let d=[{name:"",email:"",password:"",country:"",state:"",city:"",Gender:""}]
let details=[]
t=Object.keys(d[0])
l=t.length
console.log(l)



var form1=document.getElementById("form1")
console.log(form1)
var form2=document.createElement("form")
form2.setAttribute("id","form")
form1.appendChild(form2)
var form=document.getElementById("form")
var namelabel=document.createElement("label")
namelabel.innerHTML="Name          :"
namelabel.setAttribute("for","name")
form.append(namelabel)
var nameInput=document.createElement("input")
nameInput.setAttribute("type","text")
nameInput.setAttribute("id","name")
form.append(nameInput)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var emaillabel=document.createElement("label")
emaillabel.innerHTML="E-mail:        "
emaillabel.setAttribute("for","email")
form.append(emaillabel)
var emailInput=document.createElement("input")
emailInput.setAttribute("type","text")
emailInput.setAttribute("id","email")
form.append(emailInput)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var passwordlabel=document.createElement("label")
passwordlabel.innerHTML="Password:      "
passwordlabel.setAttribute("for","password")
form.append(passwordlabel)
var passwordInput=document.createElement("input")
passwordInput.setAttribute("type","password")
passwordInput.setAttribute("id","password")
form.append(passwordInput)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var rpasswordlabel=document.createElement("label")
rpasswordlabel.innerHTML="RetypePassword:"
passwordlabel.setAttribute("for","password")
form.append(rpasswordlabel)
var rpasswordInput=document.createElement("input")
rpasswordInput.setAttribute("type","password")
rpasswordInput.setAttribute("id","rpassword")
form.append(rpasswordInput)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var countrylabel=document.createElement("label")
countrylabel.innerHTML="Country:       "
form.append(countrylabel)
var countryselect=document.createElement("select")
countryselect.setAttribute("id","s")
form.append(countryselect)
var countryoption0=document.createElement("option")
countryoption0.setAttribute("value","select")
countryoption0.innerHTML="Select"
countryselect.append(countryoption0)
var countryoption1=document.createElement("option")
countryoption1.setAttribute("value","India")
countryoption1.innerHTML="india"
countryselect.append(countryoption1)
var countryoption2=document.createElement("option")
countryoption2.setAttribute("value","australia")
countryoption2.innerHTML="australia"
countryselect.append(countryoption2)
var countryoption3=document.createElement("option")
countryoption3.setAttribute("value","africa")
countryoption3.innerHTML="Africa"
countryselect.append(countryoption3)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var statelabel=document.createElement("label")
statelabel.innerHTML="State:         "
form.append(statelabel)
var stateselect=document.createElement("select")
stateselect.setAttribute("id","s1")
form.append(stateselect)
var stateoption0=document.createElement("option")
stateoption0.setAttribute("value","select")
stateoption0.innerHTML="Select"
stateselect.append(stateoption0)
var stateoption1=document.createElement("option")
stateoption1.setAttribute("value","kerla")
stateoption1.innerHTML="kerla"
stateselect.append(stateoption1)
var stateoption2=document.createElement("option")
stateoption2.setAttribute("value","delhi")
stateoption2.innerHTML="delhi"
stateselect.append(stateoption2)
var stateoption3=document.createElement("option")
stateoption3.setAttribute("value","mumbai")
stateoption3.innerHTML="mumbai"
stateselect.append(stateoption3)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var citylabel=document.createElement("label")
citylabel.innerHTML="city:          "
form.append(citylabel)
var cityselect=document.createElement("select")
cityselect.setAttribute("id","s2")
form.append(cityselect)
var cityoption0=document.createElement("option")
cityoption0.setAttribute("value","select")
cityoption0.innerHTML="Select"
cityselect.append(cityoption0)
var cityoption1=document.createElement("option")
cityoption1.setAttribute("value","chennai")
cityoption1.innerHTML="chennai"
cityselect.append(cityoption1)
var cityoption2=document.createElement("option")
cityoption2.setAttribute("value","madhurai")
cityoption2.innerHTML="madhurai"
cityselect.append(cityoption2)
var cityoption3=document.createElement("option")
cityoption3.setAttribute("value","salem")
cityoption3.innerHTML="salem"
cityselect.append(cityoption3)
var linebreak = document.createElement('br');
form.append(linebreak)
var linebreak = document.createElement('br');
form.append(linebreak)


var genderlabel=document.createElement("label")
genderlabel.innerHTML="Gender        :"
form.append(genderlabel)
var male=document.createElement("label")
male.innerHTML="male"
var genderinput1=document.createElement("input")
genderinput1.setAttribute("type","radio")
genderinput1.setAttribute("name","gender")
genderinput1.setAttribute("value","male")
genderinput1.setAttribute("class","gender")
var malelabel=document.createElement("label")
malelabel.innerHTML="Male"
malelabel.setAttribute("for","male")
form.append(malelabel)
form.append(genderinput1)
var female=document.createElement("label")
male.innerHTML="female"
var genderinput2=document.createElement("input")
genderinput2.setAttribute("type","radio")
genderinput2.setAttribute("name","gender")
genderinput2.setAttribute("value","female")
genderinput2.setAttribute("class","gender")
var femalelabel=document.createElement("label")
femalelabel.setAttribute("for","fmale")
femalelabel.innerHTML="female"
form.append(femalelabel)
form.append(genderinput2)



//FUNCTION AFTER SUBMIT BUTTON GETS CLICKED

function adddetails(){

  console.log("details")

  var gender=function(){
    var e=document.getElementsByName("gender");
    for(var i=0;i<e.length;i++){
      if(e[i].checked)
      return e[i].value
    }
    console.log(form)
      }
    let detail={
        name:document.getElementById('name').value,
        email:document.getElementById('email').value,
        password:document.getElementById('password').value,
        country:document.getElementById("s").value,
        state:document.getElementById("s1").value,
        city:document.getElementById("s2").value,
        Gender:gender()
    }
    details.push(detail)
 
    createtable()
   
    console.log("details")
    var formsubmit=document.getElementById("submit");
    function hanleform(event){event.preventDefault();}
    form.addEventListener("submit",hanleform)
    document.getElementById("form").reset()
    document.getElementById("name").focus();
    
}
//SUBMIT BUTTON
var submitelement = document.createElement('input'); 
submitelement.setAttribute("name", "dsubmit");
submitelement.setAttribute("type", "submit");
submitelement.setAttribute("value", "Submit");
submitelement.setAttribute("id", "submit");
form.appendChild(submitelement);

submitelement.addEventListener("click",adddetails)
//TABLE header
var div=document.getElementById("tab")
var table=document.createElement("table")
table.setAttribute("id","table")
div.append(table)
var thead=table.createTHead();
var tr=thead.insertRow();
for(var i=0;i<l;i++){
  var th =document.createElement("th")
  th.innerHTML=t[i]
  tr.appendChild(th)
}
var tbody=document.createElement("tbody")
tbody.setAttribute("id","tbody")
table.appendChild(tbody)
//Create table
function createtable(){
  document.getElementById("tbody").innerHTML = "";
  for(var element of details){
   
     var tr=tbody.insertRow();
     for(var e in element){
       console.log(e)
      var td=tr.insertCell();
      td.innerHTML=(element[e])
      
    

     }

  }
}








