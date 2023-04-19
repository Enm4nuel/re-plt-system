function habilitar() 
{
	edificio = document.getElementById('edificio').value;
	moneda = document.getElementById('moneda').value;
	batch = document.getElementById('batch').value;
	val = 0;

	if (edificio != "Selecciona el edificio...")
	{
		val++;
		document.getElementById('moneda').disabled = false;
	}
	else
	{
		document.getElementById('moneda').disabled = true;
		document.getElementById('moneda').value = "Selecciona la moneda...";
		document.getElementById('batch').value = "";
		document.getElementById('batch').disabled = true;
		
	}

	if (moneda != "Selecciona la moneda...")
	{
		val++;
		document.getElementById('batch').disabled = false;
	}
	else
	{
		document.getElementById('batch').disabled = true;
		document.getElementById('batch').value = "";
	}

	if (batch != null)
	{
		if (batch.length() == 8)
		{
			val++;
		}
	}
	

	if (val == 3)
	{
		document.getElementById("btn_gen_plt").disabled = false;
	}
	else
	{
		document.getElementById("btn_gen_plt").disabled = true;
	}

}

document.getElementById('edificio').addEventListener('change', habilitar);
document.getElementById('moneda').addEventListener('change', habilitar);
//document.getElementById('btn_gen_plt').addEventListener('click', ()=> {	});
