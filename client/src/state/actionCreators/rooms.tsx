import { action } from './types';
import { Dispatch } from 'redux';
import { noAuthInstance } from '../../apiService';

export const getRooms =
  () =>
  async (dispatch: Dispatch): Promise<void> => {
    try {
      dispatch({ type: action.GET_ROOMS_REQUEST });
      const { data } = await noAuthInstance.get(`api/catalog/rooms`);
      dispatch({ type: action.GET_ROOMS_SUCCESS, payload: data });
    } catch (error) {
      dispatch({
        type: action.GET_ROOMS_REQUEST_FAILED,
        error: error.message,
      });
    }
  };
