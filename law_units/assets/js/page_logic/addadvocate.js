end_point = "http://localhost:8000/"
function add_advocate(){
    alert("hii")
    var data_to_submit = {}
    data_to_submit["full_name"] = document.getElementById("full-name").value;
    data_to_submit["email"] = document.getElementById("email").value
    var inputContainer = document.getElementById('inputContainer');
    item = inputContainer.childElementCount
    list_of_item = []
    for(i=0;i<=item;i++){
        point_of_con = {}
        point_of_con["fullName"] = document.getElementById("fullName"+i).value
        point_of_con["email"] = document.getElementById("email"+i).value
        point_of_con["phoneNo"] = document.getElementById("phoneNo"+i).value
        list_of_item.push(point_of_con)
    }
    data_to_submit["point_of_con"] = list_of_item
    data_to_send={
        method : "POST",
        headers :{
            "Content-type":"application/json"
        },
        body:JSON.stringify(data_to_submit)
    }

    fetch(end_point+"home/NewAdvocate/",data_to_send)
}