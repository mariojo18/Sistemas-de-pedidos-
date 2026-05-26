import heapq
import math


class GestorGrafo:
    def __init__(self):
        self._nodos = {}       
        self._ady   = {}     


    def agregar_tienda(self, id_tienda: int, nombre: str, x: float, y: float) -> bool:
        if id_tienda in self._nodos:
            print(f"[Grafo] id={id_tienda} ya existe.")
            return False
        self._nodos[id_tienda] = {"nombre": nombre, "x": x, "y": y}
        self._ady[id_tienda]   = []
        print(f"[Grafo] Tienda '{nombre}' (id={id_tienda}) agregada.")
        return True

    def agregar_ruta(self, id_a: int, id_b: int, peso: float = None) -> bool:
        if id_a not in self._nodos or id_b not in self._nodos:
            print("[Grafo] Una o ambas tiendas no existen.")
            return False
        if any(v == id_b for v, _ in self._ady[id_a]):
            print(f"[Grafo] Ruta {id_a}↔{id_b} ya existe.")
            return False
        if peso is None:
            a, b = self._nodos[id_a], self._nodos[id_b]
            peso = math.sqrt((b["x"]-a["x"])**2 + (b["y"]-a["y"])**2)
        self._ady[id_a].append((id_b, peso))
        self._ady[id_b].append((id_a, peso))
        print(f"[Grafo] Ruta {self._nodos[id_a]['nombre']} ↔ "
              f"{self._nodos[id_b]['nombre']} (peso={peso:.2f}) agregada.")
        return True

    def eliminar_tienda(self, id_tienda: int) -> bool:
        if id_tienda not in self._nodos:
            print(f"[Grafo] id={id_tienda} no existe.")
            return False
        for vecino, _ in self._ady[id_tienda]:
            self._ady[vecino] = [(v, p) for v, p in self._ady[vecino] if v != id_tienda]
        nombre = self._nodos.pop(id_tienda)["nombre"]
        del self._ady[id_tienda]
        print(f"[Grafo] Tienda '{nombre}' eliminada.")
        return True

    def eliminar_ruta(self, id_a: int, id_b: int) -> bool:
        if id_a not in self._nodos or id_b not in self._nodos:
            print("[Grafo] Una o ambas tiendas no existen.")
            return False
        antes = len(self._ady[id_a])
        self._ady[id_a] = [(v, p) for v, p in self._ady[id_a] if v != id_b]
        self._ady[id_b] = [(v, p) for v, p in self._ady[id_b] if v != id_a]
        if len(self._ady[id_a]) == antes:
            print(f"[Grafo] No había ruta entre {id_a} y {id_b}.")
            return False
        print(f"[Grafo] Ruta {id_a}↔{id_b} eliminada.")
        return True

    def buscar_tienda(self, id_tienda: int):
        """Busca una tienda por id. O(1)"""
        n = self._nodos.get(id_tienda)
        if n:
            print(f"[Grafo] '{n['nombre']}' | pos=({n['x']},{n['y']}) "
                  f"| conexiones={len(self._ady[id_tienda])}")
        else:
            print(f"[Grafo] id={id_tienda} no encontrado.")
        return n

    def buscar_ruta(self, id_a: int, id_b: int):
        if id_a not in self._nodos or id_b not in self._nodos:
            print("[Grafo] Una o ambas tiendas no existen.")
            return None
        for vecino, peso in self._ady[id_a]:
            if vecino == id_b:
                print(f"[Grafo] Ruta directa {id_a}↔{id_b}: peso={peso:.2f}")
                return peso
        print(f"[Grafo] No hay ruta directa entre {id_a} y {id_b}.")
        return None

    def ruta_mas_corta(self, id_origen: int, id_destino: int):
        if id_origen not in self._nodos or id_destino not in self._nodos:
            print("[Grafo] Una o ambas tiendas no existen.")
            return float('inf'), []
        dist   = {n: float('inf') for n in self._nodos}
        previo = {n: None         for n in self._nodos}
        dist[id_origen] = 0
        heap = [(0, id_origen)]
        while heap:
            costo, actual = heapq.heappop(heap)
            if costo > dist[actual]:
                continue
            if actual == id_destino:
                break
            for vecino, peso in self._ady[actual]:
                nc = costo + peso
                if nc < dist[vecino]:
                    dist[vecino]   = nc
                    previo[vecino] = actual
                    heapq.heappush(heap, (nc, vecino))
        if dist[id_destino] == float('inf'):
            print(f"[Grafo] Sin camino entre {id_origen} y {id_destino}.")
            return float('inf'), []
        camino, actual = [], id_destino
        while actual is not None:
            camino.append(self._nodos[actual]["nombre"])
            actual = previo[actual]
        camino.reverse()
        print(f"[Grafo] Ruta más corta: {' → '.join(camino)} | dist={dist[id_destino]:.2f}")
        return dist[id_destino], camino

    def mostrar_grafo(self):
        if not self._nodos:
            print("[Grafo] El grafo está vacío.")
            return
        rutas = sum(len(v) for v in self._ady.values()) // 2
        print(f"\n{'='*45}\n  GRAFO — {len(self._nodos)} tiendas | {rutas} rutas\n{'='*45}")
        for id_t, n in self._nodos.items():
            print(f"  [{id_t}] {n['nombre']}  ({n['x']},{n['y']})")
            for vec, p in self._ady[id_t]:
                print(f"       ↔  {self._nodos[vec]['nombre']} (peso={p:.2f})")
        print('='*45)
