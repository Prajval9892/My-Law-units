end_point = "http://localhost:8000/"
page_number=1
function nextPage(){
page_number = page_number+1
show_table()

}

function previousPage(){
    page_number = page_number-1
    show_table()

}

window.onload = function render_table(){
    
}





function show_table(){
    var tableBody = document.getElementById('tbody_id');
console.log(tableBody)
my_param= new URLSearchParams()
my_param.append("page_number",page_number)
data_to_set = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    }

}
tableBody.innerHTML = '';
fetch(end_point+"home/team_pagi?"+my_param.toString(),data_to_set).then(data=>{
    return data.json()
}).then(new_data=>{
    for(i=0;i<=new_data.data.length-1;i++){
        var row = document.createElement('tr');
        row.innerHTML = `
        <td>${i + 1}</td>
        <td>${new_data.data[i].first_name}</td>
        <td>${new_data.data[i].last_name}</td>
        <td>${new_data.data[i].designation}</td>
        <td>${new_data.data[i].email}</td>
        <td>${new_data.data[i].number}</td>
        <td class="table-action">
            <a href="javascript: void(0);" class="action-icon"> <i class="mdi mdi-eye"></i></a>
            <a href="javascript: void(0);" class="action-icon"> <i class="mdi mdi-pencil"></i></a>
            <a href="javascript: void(0);" class="action-icon"> <i class="ri-file-paper-2-line"></i></a>
            <a href="javascript: void(0);" class="action-icon"> <i class="mdi mdi-delete"></i></a>
        </td>
    `;
    tableBody.appendChild(row);
    }

})
}