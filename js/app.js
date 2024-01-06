

const shuffleArray = (arr) => {
    for ( let i=0; i<arr.length; i++ ) {
        let j = Math.floor(Math.random()*arr.length )
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }
    return arr
}

const generateTeams = (elementsList, teamLength) => {
    const teams = [];
    if (elementsList.length < teamLength)
        return teams;
    elementsListShuffled = shuffleArray(elementsList)
    
    for (let i=0; i<elementsList.length; i=i+teamLength)
        teams.push(elementsListShuffled.slice(i, i+teamLength))
    console.log(elementsListShuffled);
    console.log(teams);
}

generateTeams(['1', '2', '3', '4', '5', '6'], 2)