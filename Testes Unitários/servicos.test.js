const axios = require("axios");

const URL = "http://localhost:3000/api";

let auth_token = "";

const login = {
    "email": "admin@salaofiquebella.com",
    "senha": "admin123"
};

describe("GET: /servicos", () => {
    beforeAll(async () => {
        const response = await axios.post(`${URL}/auth/login`, login); // post na rota de login para obter o token
    auth_token = response.data.session.access_token;                // atribuindo o token à variavel
        expect(auth_token).toBeTruthy();                            // assert auth_token is true
    });

    test("ENTRADA INVÁLIDA: Usuário não autenticado.", async () => {
        await expect(axios.get(`${URL}/servicos/list`)).rejects.toHaveProperty("response.status", 401); // assert status == 401
    });

    test("CAMINHO FELIZ: Listar os serviços.", async () => {
        const config = {                                            // config para enviar o token na req
            headers: {
                "Authorization": `Bearer ${auth_token}`
            }
        }
        const response = await axios.get(`${URL}/servicos/list`, config);
        expect(response.status).toBe(200);                          // assert Status == 200
        expect(Array.isArray(response.data)).toBe(true);            // assert isArray == true
        expect(response.data.length).toBeGreaterThan(0);            // assert length > 0
    });

    test("CAMINHO ALTERNATIVO: Listar um serviço.", async () => {
        const config = {                                            // config para enviar o token na req
            headers: {
                "Authorization": `Bearer ${auth_token}`
            }
        }
        const id = "e40d2776-61a2-4370-b103-a53f44087f72";
        const response = await axios.get(`${URL}/servicos/list/${id}`, config);
        expect(response.status).toBe(200);                          // assert Status == 200
        expect(response.data[0].nome).toBe("Luzes");                // assert nome == Luzes
        expect(response.data.length).toBe(1);                       // assert length == 1
    });
});

// describe("POST: /servicos");

// describe("PATCH: /servicos");

// describe("DELETE: /servicos");