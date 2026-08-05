document.addEventListener("DOMContentLoaded", function () {
  const mapElement = document.getElementById("mapa");
  if (!mapElement) return;

  // 1. Lê os dados embutidos na tag JSON do Django
  const dadosElement = document.getElementById("dados-mapa-json");
  if (!dadosElement) return;

  const ocorrencias = JSON.parse(dadosElement.textContent);

  // 2. Inicializa o Mapa (Juazeiro - BA)
  const map = L.map("mapa").setView([-9.4137, -40.5036], 13);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "© OpenStreetMap",
  }).addTo(map);

  // 3. Desenha os marcadores
  ocorrencias.forEach((item) => {
    const lat = parseFloat(item.lat);
    const lng = parseFloat(item.lng);

    if (!isNaN(lat) && !isNaN(lng)) {
      L.marker([lat, lng]).addTo(map).bindPopup(`
                    <div style="font-family: sans-serif; min-width: 150px;">
                        <strong style="color: #d9534f; font-size: 14px;">⚠️ ${item.bairro}</strong><br>
                        <small class="text-muted"><b>Data/Hora:</b> ${item.data_hora}</small><br>
                        <p style="margin: 6px 0 0 0; font-size: 13px;">${item.descricao}</p>
                    </div>
                `);
    }
  });

  setTimeout(() => {
    map.invalidateSize();
  }, 300);
});
