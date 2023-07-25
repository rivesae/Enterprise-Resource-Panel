//  JavaScript code to handle the clearing chaindown selectors of brand - item - cost
function clear_item_cost() {
  const form = document.getElementById('Selector');
  const inputNames = ['cost_value', 'package'];
  const selectNames = ['item_value'];

  for (let i = 0; i < form.elements.length; i++) {
    const element = form.elements[i];
    if (element.name && inputNames.includes(element.name) && element.tagName === 'INPUT') {
      element.value = '';
    }  else if (element.name && selectNames.includes(element.name) && element.tagName === 'SELECT') {
      element.selectedIndex = 0;
    }
  }
}

function clear_cost() {
  const form = document.getElementById('Selector');
  const inputNames = ['cost_value'];

  for (let i = 0; i < form.elements.length; i++) {
    const element = form.elements[i];
    if (element.name && inputNames.includes(element.name) && element.tagName === 'INPUT') {
      element.value = '';
    }
  }
}
