function habilitar() 
{
	edificio = document.getElementById('edificio').value;
	moneda = document.getElementById('moneda').value;
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
	}

	if (moneda != "Selecciona la moneda...")
	{
		val++;
	}
	

	if (val == 2)
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
