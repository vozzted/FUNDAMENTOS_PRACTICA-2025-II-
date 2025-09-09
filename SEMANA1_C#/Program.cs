using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer2();
            Console.ReadKey();
        }
        static void ejer1()
        {
            string nombre, carrera;

            Console.Write("cual es tu nombre: ");
            nombre = Console.ReadLine();
            Console.Write("cual es tu carrera: ");
            carrera = Console.ReadLine();

            Console.WriteLine(nombre + ", Bienvenido al curso de fundamentos de algoritmos de la carrera " + carrera);
            Console.ReadKey();
        }
        static void ejer2()
        {
            Console.Write("Ingrese un numero x: ");
            int x = int.Parse(Console.ReadLine());
            Console.Write("Ingrese un numero y: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double resu = (double)x / (double)y;

            Console.WriteLine("Sumass: " +(x+y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicación: " + (x * y));
            Console.WriteLine("División: " + resu );

        }
        static void ejer3()
        {


        }

    }
}
