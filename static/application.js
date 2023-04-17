
$(document).ready(function() {
  // Sélectionne tous les éléments de message flash avec la classe "alert-dismissible"
  $(".alert-dismissible").each(function() {
    // Définir une durée d'attente de 5 secondes avant de supprimer l'élément
    setTimeout(function() {
      // Supprimer l'élément parent de l'élément actuel
      $(this).parent().remove();
    // Attendre 5 secondes avant d'exécuter cette fonction
    }, 5000);
  });
});


