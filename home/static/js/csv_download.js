function habilitar() 
{
	edificio = document.getElementById('edificio').value;
	moneda = document.getElementById('moneda').value;
	batch = document.getElementById('batch').value;
	val = 0;
	console.log(batch)

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
		document.getElementById('batch').value = "";
		document.getElementById('batch').disabled = true;
	}

	if (batch != "")
	{
		if (batch.length == 8)
		{
			val++;
		}
	}
	

	if (val >= 3)
	{
		document.getElementById("btn_gen_plt").disabled = false;
	}
	else
	{
		document.getElementById("btn_gen_plt").disabled = true;
	}
}

function validationData()
{
	// mensaje como respuesta al validar
	valid = "<i class='bi bi-check-lg text-success h-5'> </i>";
	invalid = "<i class='bi bi-x-lg text-danger h-5'> </i>";

	// mensaje como respuesta extra al validar id de batch
	incomplete_id = "<p>Numero de batch incompleto. </p>";
	empty_id = "<p>Numero de batch vacio. </p>";
	veryLong_id = "<p>Numero de batch muy largo. </p>";
	correct_id = "<p>Numero de batch correcto. </p>"

	// extraer la informacion de data de cada input
	edificio = document.getElementById('edificio').value;
	moneda = document.getElementById('moneda').value;
	batch = document.getElementById('batch').value;

	// Validacion - Edificio
	if (edificio != "Selecciona el edificio...")
	{
		document.getElementById("valid-edificio").innerHTML = valid;
	}
	else
	{
		document.getElementById("valid-edificio").innerHTML = invalid;
	}

	// Validacion - Moneda
	if (moneda != "Selecciona la moneda...")
	{
		document.getElementById("valid-moneda").innerHTML = valid;
	}
	else
	{
		document.getElementById("valid-moneda").innerHTML = invalid;
	}

	// Validacion - Batch
	if (batch != "")
	{
		if (batch.length == 8)
		{
			document.getElementById("valid-batch").innerHTML = valid+correct_id;
		}
		else if (batch.length > 8)
		{
			document.getElementById("valid-batch").innerHTML = invalid+veryLong_id;
		}
		else
		{
			document.getElementById("valid-batch").innerHTML = invalid+incomplete_id;
		}
	}
	else
	{
		document.getElementById("valid-batch").innerHTML = invalid+empty_id;
	}
}

// funcion habilitar
document.getElementById('edificio').addEventListener('change', habilitar);
document.getElementById('moneda').addEventListener('change', habilitar);
document.getElementById('batch').addEventListener('input', habilitar);

// funcion validacion
document.getElementById('edificio').addEventListener('change', validationData);
document.getElementById('moneda').addEventListener('change', validationData);
document.getElementById('batch').addEventListener('input', validationData);

// Al iniciar la vista
document.getElementById("valid-edificio").innerHTML = "<i class='bi bi-x-lg text-danger h-5'> </i>";
document.getElementById("valid-moneda").innerHTML = "<i class='bi bi-x-lg text-danger h-5'> </i>";
document.getElementById("valid-batch").innerHTML = "<i class='bi bi-x-lg text-danger h-5'> </i>"+"<p>Numero de batch vacio. </p>";