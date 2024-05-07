end_point = "http://127.0.0.1:8000/"
function submit_to_do(){
    
    data_to_submit = {}
    data_to_submit["description"] = document.getElementById("description").value
    data_to_submit["start_date"] = document.getElementById("start_date").value
    data_to_submit["end_date"] = document.getElementById("end_date").value
    data_to_submit["case_name"] = document.getElementById("case_name").value
    data_to_submit["advocate"] = document.getElementById("advocate").value
    data_to_send = {
        "method":"POST",
        "Content-type":"Application/json",
        body:JSON.stringify(data_to_submit)
    }
    fetch(end_point+"home/add_todo",data_to_send).then(data=>{
        return data.json()
    }).then(parse_data=>{
        if(parse_data.status==200){
            const toast = document.getElementById('toast');
            toast.classList.remove('hidden');
            showToast(parse_data.message,"#76eb6a")
            $('#add-new-task-modal').modal('hide');
        }
        else{
            const toast = document.getElementById('toast');
            toast.classList.remove('hidden');
            showToast(parse_data.message,"#f25544")
        }
        
    })
    location.reload();

}

function showToast(message,color) {
    var toast = document.getElementById("toast");
    toast.className = "show";
    toast.innerText = message;
    toast.style.backgroundColor = color
    setTimeout(function(){ toast.className = toast.className.replace("show", "dssssssssssssss"); }, 3000);
  }


  function change_status(status,id){
    data_to_send = {"status":status,"id":id}
    data_to_set = {
        method: "POST",
        "Content-Type": "application/json",
        body:JSON.stringify(data_to_send)
    }
    fetch(end_point+"home/change_to_do_status",data_to_set).then(data=>{
        return data.json()
    }).then(parse_data=>{
        if(parse_data.status==200){
            div_tag = document.getElementById(id)
            if(div_tag.classList.contains("bg-danger-lighten")){
                div_tag.classList.remove("bg-danger-lighten")  
            }
            else if(div_tag.classList.contains("bg-warning-lighten")){
                div_tag.classList.remove("bg-warning-lighten")  

            }
            else if(div_tag.classList.contains("bg-success-lighten")){
                div_tag.classList.remove("bg-success-lighten")  

            }
            
            if(status=="pending"){
                div_tag.classList.add("bg-danger-lighten")
            }
            else if(status=="comp"){
                div_tag.classList.add("bg-success-lighten")
            }
            const toast = document.getElementById('toast');
            toast.classList.remove('hidden');
            showToast(parse_data.message,"#76eb6a")
        }
        else{
            const toast = document.getElementById('toast');
            toast.classList.remove('hidden');
            showToast(parse_data.message,"#f25544")
        }
        
    })
  }