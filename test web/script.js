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
        // $(html).toggleClass("changemode");
    })
});