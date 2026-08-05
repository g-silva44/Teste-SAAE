document.addEventListener("DOMContentLoaded", function () {
  const mapElement = document.getElementById("mapa");
  if (!mapElement) return;

  // Inicializa o Mapa centrando em Juazeiro
  const map = L.map("mapa").setView([-9.4137, -40.5036], 13);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "© OpenStreetMap",
  }).addTo(map);

  // Carrega as ocorrências iniciais
  const dadosElement = document.getElementById("dados-mapa-json");
  if (dadosElement) {
    const ocorrenciasIniciais = JSON.parse(dadosElement.textContent);
    ocorrenciasIniciais.forEach((item) => adicionarMarcador(item));
  }

  // Função utilitária para criar o pino no Leaflet
  function adicionarMarcador(item) {
    const lat = parseFloat(item.lat);
    const lng = parseFloat(item.lng);

    if (!isNaN(lat) && !isNaN(lng)) {
      const marker = L.marker([lat, lng]).addTo(map);

      marker.bindPopup(`
                <div style="font-family: sans-serif; min-width: 150px;">
                    <strong style="color: #d9534f; font-size: 14px;">⚠️ ${item.bairro}</strong><br>
                    <small class="text-muted"><b>Data/Hora:</b> ${item.data_hora}</small><br>
                    <p style="margin: 6px 0 0 0; font-size: 13px;">${item.descricao}</p>
                </div>
            `);
      return marker;
    }
  }

  // Conexão em tempo real
  const evtSource = new EventSource("/stream-ocorrencias/");

  evtSource.onmessage = function (event) {
    const novaOcorrencia = JSON.parse(event.data);

    // Adiciona o novo pino no mapa
    const novoMarcador = adicionarMarcador(novaOcorrencia);

    if (novoMarcador) {
      // Centraliza o mapa no novo ponto e abre o balão de alerta
      map.flyTo([novaOcorrencia.lat, novaOcorrencia.lng], 14);
      novoMarcador.openPopup();
    }
  };

  setTimeout(() => {
    map.invalidateSize();
  }, 300);
});
