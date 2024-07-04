function validar(){
  var form = document.form;
  var isValid = true;

  // Limpiar mensajes de error anteriores
  var errorMessages = document.querySelectorAll('.error-message');
  errorMessages.forEach(function(message) {
      message.textContent = '';
  });

  // Validar todos los campos
  isValid &= validateField(form.nombre, validateNombre);
  isValid &= validateField(form.appaterno, validateApellido);
  isValid &= validateField(form.apmaterno, validateApellido);
  isValid &= validateField(form.rut, validateRut);
  isValid &= validateField(form.edad, validateEdad);
  isValid &= validateField(form.telefono, validateTelefono);

  return Boolean(isValid); // Convertir a booleano para asegurar que sea true/false
}

function validateField(field, validator) {
  var errorDiv = field.nextElementSibling;
  var errorMessage = validator(field.value.trim());
  if (errorMessage) {
      errorDiv.textContent = errorMessage;
      return false;
  } else {
      errorDiv.textContent = '';
      return true;
  }
}

function validateNombre(value) {
  if (value.length === 0) {
      return "El campo nombre está vacío";
  } else if (value.length < 3 || value.length > 20) {
      return "El nombre debe tener entre 3 y 20 caracteres";
  }
  return null;
}

function validateApellido(value) {
  if (value.length === 0) {
      return "El campo Apellido está vacío";
  } else if (value.length < 3 || value.length > 20) {
      return "El Apellido debe tener entre 3 y 20 caracteres";
  }
  return null;
}

function validateRut(value) {
  if (value.length === 0) {
      return "Debe ingresar el RUT";
  } else if (value.length < 9 || value.length > 10) {
      return "El RUT debe tener entre 9 y 10 caracteres";
  }
  return null;
}

function validateEdad(value) {
  var edad = parseInt(value);
  if (isNaN(edad) || edad < 18 || edad > 35) {
      return "La edad debe estar entre los 18 y los 35 años";
  }
  return null;
}

function validateTelefono(value) {
  if (value.length < 9 || value.length > 12 || isNaN(value)) {
      return "El número de teléfono debe tener entre 9 y 12 dígitos";
  }
  return null;
}

// Añadir eventos de entrada en tiempo real para cada campo
document.addEventListener('DOMContentLoaded', function() {
  var form = document.form;

  form.nombre.addEventListener('input', function() {
      validateField(form.nombre, validateNombre);
  });

  form.appaterno.addEventListener('input', function() {
      validateField(form.appaterno, validateApellido);
  });

  form.apmaterno.addEventListener('input', function() {
      validateField(form.apmaterno, validateApellido);
  });

  form.rut.addEventListener('input', function() {
      validateField(form.rut, validateRut);
  });

  form.edad.addEventListener('input', function() {
      validateField(form.edad, validateEdad);
  });

  form.telefono.addEventListener('input', function() {
      validateField(form.telefono, validateTelefono);
  });
});
