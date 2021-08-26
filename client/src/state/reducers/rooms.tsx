import { action as Action } from '../actionCreators/types';
import { RoomState, Room } from '../../type/types';

const emptyDataArr: Room[] = [];

const initialState = {
  rooms: emptyDataArr,
  loading: false,
  err: false,
};

type ActionType = {
  type: string;
  payload?: Room[];
  error?: '';
};

export const rooms = (state: RoomState = initialState, action: ActionType) => {
  if (action.type === Action.GET_ROOMS_REQUEST)
    return { loading: true, err: false };
  if (action.type === Action.GET_ROOMS_SUCCESS)
    return { ...state, loading: false, rooms: action.payload };
  if (action.type === Action.GET_ROOMS_REQUEST_FAILED)
    return { ...state, loading: false, err: true, errMessage: action.error };
  return state;
};
