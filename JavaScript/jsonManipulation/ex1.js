var obj = {name : "RajiniKanth", age : 33, hasPets : false};
var s = JSON.stringify(obj)


function printAllValues(obj){
var o = JSON.parse(s)

 var obj1=[]
for (x in o){
   obj1.push((o[x]));
   
}
console.log(obj1)
}
printAllValues();



