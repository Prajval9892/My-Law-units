end_point = "http://localhost:8000/"
function add_team(){
    var inputContainer = document.getElementById('inputContainer');
    item = inputContainer.childElementCount
    item_list=[]
    for(i=0;i<=item;i++){
        var data_to_submit = {}
        data_to_submit["firstName"] = document.getElementById("firstName"+i).value;
        data_to_submit["email"] = document.getElementById("email"+i).value
        item_list.push(data_to_submit)
    }
    console.log(item_list
    )
    

    data_to_send={
        method : "POST",
        headers :{
            "Content-type":"application/json"
        },
        body:JSON.stringify(item_list)
    }

    fetch(end_point+"home/addmember/",data_to_send)
}