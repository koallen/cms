var currentURL = "http://localhost:8888/api/reports/";
var type = "";
var preURL;
var nextURL;
var newestDataId;


pullReports();

setInterval(checkUpdate, 5000);

function checkUpdate(){
  $.ajax({
    type: "GET",
    dataType: "json",
    url: currentURL,
    success: function(data){
      if (newestDataId != data.results[0].id) {
          $("#new-notification").html("<input class='btn btn-info col-md-4' type='button' value='New Reports Available! Click to Update!' onclick='pullReports();'>");
      }
    }
  });
}

function pullReports() {
  var urlToRequest;

  if (type != "") {
    urlToRequest = addParameter(currentURL, "type", type, false);
  } else {
    urlToRequest = currentURL;
  }

  $.ajax({
    type: "GET",
    dataType: "json",
    url: urlToRequest,
    success: function(data){
      var html = '';
      preURL = data.previous;
      nextURL = data.next;
      newestDataId = data.results[0].id;
      $("#new-notification").html("");
      for (var x = 0; x < data.results.length; x++) {
        html += "<tr id='row" + data.results[x].id + "'>";
        html += "<th class='col-md-1'>";
        html += data.results[x].name;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].location;
        html += "</th><th class='col-md-3'>";
        html += data.results[x].description;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].type_of_assistance;
        html += "</th><th class='col-md-2'>";
        html += data.results[x].type_of_crisis;
        html += "</th><th class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-success' onClick='updateReportStatus(this.id, true)'><span class='glyphicon glyphicon-ok'></span>&nbsp;</button>"
        html += "</th><th class='col-md-1'><button style='width:100%;' type='button' id='" + data.results[x].id + "' class='btn btn-xs btn-danger' onClick='updateReportStatus(this.id, false)'><span class='glyphicon glyphicon-remove'></span>&nbsp;</button>"
        html += "</th></tr>";
      }
      $("#ReportContent").html(html);
      if (preURL == null){
        $("#prepage").attr("class", "disabled");
      }
      else{
        $("#prepage").attr("class", "active");
      }
      if (nextURL == null){
        $("#nextpage").attr("class", "disabled");
      }
      else{
        $("#nextpage").attr("class", "active");
      }

    }
  });
}

function updateReportStatus(reportID, newStatus) {
  var csrf_token = getCookie("csrftoken");
  var dataToPost = {"status": newStatus}
  $.ajax({
    url: "http://localhost:8888/api/reports/"+reportID+"/",
    headers: {"X-CSRFToken": csrf_token},
    data: JSON.stringify(dataToPost),
    method: "PATCH",
    contentType: 'application/json',
    dataType: "json",
    success: function(data) {
      pullReports();
      console.log("Report status updated");
    }
  });
}

function changeType() {
  type = $("#type-filter").val();
  console.log(type);
  pullReports();
}

function prePage(){
    currentURL = preURL;
    pullReports();
}

function nextPage(){
    currentURL = nextURL;
    pullReports();
}
