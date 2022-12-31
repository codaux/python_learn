function kimai_phab_to_kim(phab) {
    //find kimai id related to phabricator task_id that starts with "T".
  
    var response = UrlFetchApp.fetch('https://farasoo.kimai.ir/api/projects?&begin=2022-04-30T00:00:00&end=2022-06-13T23:59:59' , {
      headers: { 'X-AUTH-USER': 'rezasamani', 'X-AUTH-TOKEN': '111222reza' } 
    })
  
    var json = response.getContentText();
    var data = JSON.parse(json);
  
  
    var reza = data.filter( function(data){ return data.id == '2891' } );
    
  
    console.log(reza.filter(function(reza){return reza.name}));
  
  }