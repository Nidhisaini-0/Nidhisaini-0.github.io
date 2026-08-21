document.addEventListener("DOMContentLoaded", function () {

  const toc = document.getElementById("toc");
  const article = document.querySelector(".article-content");

  if (!toc || !article) {
    return;
  }


  const headings = article.querySelectorAll("h2, h3");


  if (headings.length === 0) {
    toc.parentElement.style.display = "none";
    return;
  }


  const list = document.createElement("ul");


  headings.forEach(function (heading, index) {

    if (!heading.id) {

      const slug = heading.textContent
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, "-");

      heading.id = slug || `heading-${index}`;

    }


    const item = document.createElement("li");

    if (heading.tagName === "H3") {
      item.classList.add("toc-subitem");
    }


    const link = document.createElement("a");

    link.href = "#" + heading.id;

    link.textContent = heading.textContent;


    item.appendChild(link);

    list.appendChild(item);

  });


  toc.appendChild(list);

});
