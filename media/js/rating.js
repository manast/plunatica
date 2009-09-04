var starSaves = new Hash();

function hoverStar(id, pos, imageurl)
{
	var starStrip = $(id+"-stars");
	
	if (starSaves.keys().indexOf(id) == -1)
	{
	   var starSave = new Array();
	   var imgs = starStrip.select("img")
	   for (var i = 0; i < imgs.length; i++)
	   {
			starSave[starSave.length] = imgs[i].src;
			if (i < pos)
				imgs[i].src = imageurl + "/images/star_1.0.png";
			else
			    imgs[i].src = imageurl + "/images/star_0.0.png";
	   }
	   starSaves.set(id, starSave);
	}
}

function clickStar(id, pos, imageurl)
{
	new Ajax.Request('/rating/', 
	                 { 
	                   onSuccess: function(transport){
                               //         var response = transport.responseText || "no response text";
                               //         alert("Success! \n\n" + response);
                                    },
                       parameters:{vote:pos, object:id}
                            }
                       );

	$(id +"-stars").hide()	
	$(id +"-text").update('Thanks for your vote!')
	
	starSaves.unset(id);
}

function restoreStar(id)
{
	srcs = starSaves.get(id);
	if (srcs == undefined)
		return;
	var starStrip = $(id+"-stars");
	var imgs = starStrip.select("img");
	for (var i = 0; i < srcs.length; i++)
	{
		imgs[i].src = srcs[i];
	}
	starSaves.unset(id);
}

function voteCompleted()
{
    
}
