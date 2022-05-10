$(document).ready(function()
{
    $(window).scroll(function()
    {
        if(this.scrollY>20)
        {
            $(".navbar").addClass("sticky");
        }
        else
        {
            $(".navbar").removeClass("sticky");
        }
    });

    $(".menu-btn").click(function()
    {
        $(".navbar .menu").toggleClass("active");
        $(".menu-btn i").toggleClass("active");
        $(".dark-mode-btn i").toggleClass("active");
    })

    $(".dark-mode-btn").click(function()
    {
        $(".dark-mode-btn i").toggleClass("active2");
    })
});

const themeButton = document.getElementById("theme-button");
const darkTheme = "dark-theme";

const selectedTheme = localStorage.getItem("selected-theme");

const getCurrentTheme = () =>
    document.body.classList.contains(darkTheme) ? "dark" : "light";

if (selectedTheme)
{
    document.body.classList[selectedTheme === "dark" ? "add" : "remove"](
    darkTheme
    );
}

themeButton.addEventListener("click", () =>
{
    document.body.classList.toggle(darkTheme);
    localStorage.setItem("selected-theme", getCurrentTheme());
});

// setInterval(function myTimer()
// {
//     document.getElementById("textarea").innerHTML = "Ishaan" + "'s attendance has been marked!";
// },1000);

// function csvToArray(str, delimiter = ",")
// {
//     const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
//     const rows = str.slice(str.indexOf("\n") + 1).split("\n");
//     const arr = rows.map(function (row)
//     {
//         const values = row.split(delimiter);
//         const el = headers.reduce(function (object, header, index)
//         {
//             object[header] = values[index];
//             return object;
//         }, {});
//         return el;
//     });
//     return arr;
// }
// reader.onload = function (e)
// {
//     const text = e.target.result;
//     const data = csvToArray(text);
//     document.write(JSON.stringify(data));
// };
csvpath = "records/Attendance - 02-04-2022.csv";