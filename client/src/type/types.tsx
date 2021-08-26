export type Room = {
  id: number;
  availableAt: null | string;
  category: string;
  createdAt: string;
  createdBy: number;
  description: string;
  guest: null | string;
  image: string;
  name: string;
  numReviews: number;
  price: string;
  rating: string;
  roomType: number;
  status: string;
};

export type RoomState = {
  rooms?: Room[];
  loading: boolean;
  err: boolean;
  errMessage?: string;
};
