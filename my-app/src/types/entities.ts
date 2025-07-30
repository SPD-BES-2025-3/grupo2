export type Movie = {
  id: string;
  titulo: string;
  duracao_minutos: number;
  classificacao_indicativa: string;
  poster?: string;
  generos: string[];
};

export type Session = {
  id: string;
  filme_id: string;
  data: string;
  hora: string;
  preco_por_veiculo: number;
};

export type Reservation = {
  id: string;
  sessao_id: string;
  cliente_id: string;
  placa: string;
  status: string;
  data_reserva: string;
};
