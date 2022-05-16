using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace client
{
    internal class Misurazioni
    {
        public string token { get; set; } = "24705669ef817555487499e723bb00c11656eec404fcd264c899af337d813bfaea5975ef6544214381c61ccdf49dde61984b2bb3b1c1595b9010906011be6cbc";
        public int idSilos { get; set; }
        public double ph { get; set; }
        public double tempInt { get; set; }
        public double tempEst { get; set; }
        public double umiditaInt { get; set; }
        public double umiditaEst { get; set; }
        public double pressioneInt { get; set; }
        public double livelloSensore1 { get; set; }
        public double livelloSensore2 { get; set; }
        public double livelloSensore3 { get; set; }
        public DateTime oraInvio { get; set; }
    }
}
