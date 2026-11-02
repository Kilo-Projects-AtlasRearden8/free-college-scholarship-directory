(function () {
  var index = window.SEARCH_INDEX || [];
  var input = document.getElementById("search-input");
  var resultsEl = document.getElementById("search-results");

  if (!input || !resultsEl) {
    return;
  }

  function tokenize(text) {
    return text.toLowerCase().split(/\s+/).filter(Boolean);
  }

  function score(page, queryTokens) {
    var haystack = (page.title + " " + page.excerpt).toLowerCase();
    var score = 0;
    var matched = 0;
    queryTokens.forEach(function (token) {
      if (haystack.indexOf(token) !== -1) {
        matched += 1;
        if (page.title.toLowerCase().indexOf(token) !== -1) {
          score += 2;
        }
      }
    });
    return matched === queryTokens.length ? score : -1;
  }

  function render(query) {
    var q = (query || "").trim();
    resultsEl.innerHTML = "";
    if (!q) {
      return;
    }
    var tokens = tokenize(q);
    var hits = index
      .map(function (page) {
        return { page: page, s: score(page, tokens) };
      })
      .filter(function (h) {
        return h.s >= 0;
      })
      .sort(function (a, b) {
        return b.s - a.s;
      })
      .slice(0, 10);
    if (hits.length === 0) {
      resultsEl.innerHTML = '<p class="empty">No results found.</p>';
      return;
    }
    hits.forEach(function (h) {
      var page = h.page;
      var el = document.createElement("div");
      el.className = "result";
      el.innerHTML =
        '<a href="' + page.url + '">' + escapeHtml(page.title) + "</a>" +
        '<p>' + escapeHtml(page.excerpt) + "</p>";
      resultsEl.appendChild(el);
    });
  }

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  var timer;
  input.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(function () {
      render(input.value);
    }, 120);
  });
})();
