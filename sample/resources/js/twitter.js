$(document).ready(function()
{
	var target   = $("#services-twitter-container > div")
	var template = $("#template-tweet").html()
	$.ajax({
			url: "/services/twitter",
	   dataType: "json",
		success: function(data)
		{
			for(;;)
			{
				tweet     = data.shift()
				var model = {"text": tweet.text}
				target.append(Mustache.to_html(template, model))

				if(data.length == 0)
				{
					break;
				}
			}
		}
	});
})