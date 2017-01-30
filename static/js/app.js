let eventSrc = new EventSource(ENTRIES.stream);
eventSrc.addEventListener('greeting', (event) => {
  let data = JSON.parse(event.data);
  console.log(data);
});
