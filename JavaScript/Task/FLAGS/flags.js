function flag(){
fetch('https://restcountries.eu/rest/v2/all')
.then(res=>res.json())
.then(b=>{
  function va(n){
    console.log(b[i])
  }
    for(var i=0;i<20;i++)
    {
        
       var img=document.createElement("img");
       var x=(b[i]["flag"]);
       img.src= x
       var id=document.querySelector("#container");
       id.appendChild(img);
       img.id=i
       console.log(img.id)
       img.addEventListener("click", e=> {
          var c= (b[e.target.id]);
          document.write(("<center>" +"Name: "+c["name"]+"<br>"+"AlphaCode: "+c["alpha2Code"]+"<br>"+"Capital: "+c["capital"]+"<br>"+"Region: "+c["region"]+"<br>"+"Borders: "+c["borders"]).fontcolor("tan" ));
       })
       img.addEventListener("mouseover",r=>{
        var c2= (b[r.target.id]);
        //document.querySelector("#container").textContent="hey"
        console.log("Name: "+c2["name"])


       })
  }
})
}
flag()