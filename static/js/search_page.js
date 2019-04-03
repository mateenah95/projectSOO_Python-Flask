const log = console.log

$(function() {
  const nameInputBox = $('#name-input-box');
  const delegationDropdown = $('#delegation-dropdown');

  $('.dropdown li').click(function() {
    $(this).parents('.dropdown').find('.btn').text($(this).text());
  });

  $('#searchBtn').click(searchQuery);

  $('#searchBtn').click(function() {
  });

  function getCheckedType() {
    if ($("#player-opt").is(":checked")) {
      return 'Player';
    }

    else if ($("#team-opt").is(":checked")) {
      return 'Team';
    }
  }

  function getSearchParameters() {
    const type = getCheckedType();
    const name = nameInputBox.val();

    return {'type': type, 'name': name};
  }

  function searchQuery() {
    const url = '/search_query';

    let reqBody = getSearchParameters();

    const request = new Request(url, {
      method: 'post',
      body: JSON.stringify(reqBody),
      headers: {
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json'
      },
    })

    // A 'fetch' AJAX call to the server.
    fetch(request)
    	.then((res) => {
          return res.json()
      })
      .then((jsonResult) => {
        if (jsonResult.length === 0) {
          displayNoResults();
        }
        else {
          displaySearchResults(jsonResult);
        }
      }).catch((error) => {
      	// if an error occured it will be logged to the JavaScript console here.
          console.log("An error occured with fetch:", error)
      })
  }

  function displayNoResults() {
    const markup = `
      <div class='alert alert-primary col-md-12'>
        No results found
      </div>
    `
    $('#search-results-container').html(markup);
  }

  function displaySearchResults(searchResults) {
    for (let i = 0; i < searchResults.length; i++) {
      displaySingleResult(searchResults[i]);
    }
  }

  function displaySingleResult(resultObj) {
    if (getCheckedType() === 'Player') {
      displayAthlete(resultObj);
    }
    else {
      displayTeam(resultObj);
    }
  }

  function displayAthlete(athlete) {
    const markup = `
      <div class='alert alert-primary col-md-12'>
        <a href="player/${athlete.name}">${athlete.name}</a>
        ${athlete.province}
        ${athlete.sport}
      </div>
    `
    $('#search-results-container').html(markup);
  }

  function displayTeam(team) {
    const markup = `
      <div class='alert alert-primary col-md-12'>
        <a href="team/${team.sport}/${team.name}">${team.name}</a>
        ${team.province}
        ${team.sport}
      </div>
    `
    $('#search-results-container').html(markup);
  }
})
