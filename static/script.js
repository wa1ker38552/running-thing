function searchRunner() {
    window.location.href = "/search/runner?q="+runnerSearch.value
}

function searchMeet() {
    window.location.href = "/search/meet?q="+runnerSearch.value
}


function setupSearch(type) {
    runnerSearch = dquery("#runner-search")
    runnerSearch.onchange = function() {
        window.location.href = `/search/${type}?q=${runnerSearch.value}`
    }
}

function searchRunner() {
    window.location.href = "/search/runner?q="+runnerSearch.value
}

function setupSearch(type) {
    runnerSearch = dquery("#runner-search")
    runnerSearch.onchange = function() {
        window.location.href = `/search/${type}?q=${runnerSearch.value}`
    }
}

const formatDate = (date) => {
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const year = date.getFullYear();
    return `${month}/${day}/${year}`;
};

const getRelativeTime = (timestamp) => {
    date = new Date(timestamp)
    const now = new Date();
    const seconds = Math.floor((now - date) / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (seconds < 60) return `${seconds} second(s) ago`;
    if (minutes < 60) return `${minutes} minute(s) ago`;
    if (hours < 24) return `${hours} hour(s) ago`;
    return `${days} day(s) ago`;
};

function renderRunner(item) {
    const e = dcreate("a", "runner-result", `
        <div class="centered-vertically">
            <div class="tag ${item.division.split(" ").join("-")}">${item.division}</div>
            <h3>${item.name} - ${item.age}</h3>
        </div>
        <h4>${item.team}</h4>
    `)
    e.href = "/runner?id="+item.id
    return e
}

function renderMeet(item) {
    const e = dcreate("a", "meet", `
        <h3>${item.name}</h3>
        <h4>${getRelativeTime(item.time)}</h4>
        <h4>${item.schools[0]} vs ${item.schools[1]}</h4>
    `)
    e.href = "/meet?id="+item.id
    return e
}

const formatSeconds = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
};

function renderTopRunner(index, item) {
    const e = dcreate("a", "top-runner", `
        <h2 class="centered-vertically" style="gap: 0.5rem">#${index+1} ${item.name}</h2>
        <h3>Time: ${formatSeconds(item.time)}</h3>    
    `)
    e.href = "/runner?id="+item.id
    return e
}