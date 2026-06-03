from database import get_connection

try:
    conn = get_connection()
    print("Conexão com Supabase realizada com sucesso!")
    conn.close()
except Exception as e:
    print("Erro:", e)