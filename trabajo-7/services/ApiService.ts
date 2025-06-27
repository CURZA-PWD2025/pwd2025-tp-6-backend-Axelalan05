import axios, { type AxiosResponse } from 'axios';

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export default {
    getAll<T>(resource: string): Promise<AxiosResponse<T>> {
        return apiClient.get(`/${resource}/`);
    },
    getOne<T>(resource: string, id: number | string): Promise<AxiosResponse<T>> {
        return apiClient.get(`/${resource}/${id}`);
    },
    create<T>(resource: string, data: T): Promise<AxiosResponse<T>> {
        return apiClient.post(`/${resource}/`, data);
    },
    update<T>(resource: string, id: number | string, data: T): Promise<AxiosResponse<T>> {
        return apiClient.put(`/${resource}/${id}`, data);
    },
    destroy<T>(resource: string, id: number | string): Promise<AxiosResponse<T>> {
        return apiClient.delete(`/${resource}/${id}`);
    }
};