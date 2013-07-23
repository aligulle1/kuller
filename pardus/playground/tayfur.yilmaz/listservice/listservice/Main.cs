using System;
using System.Management;
using System.Collections;
using System.Diagnostics;

namespace listservice
{
	class MainClass
	{
		public static void getServiceList()
		{
			Process [] getService = Process.GetProcesses() ;
			foreach(var item in getService)
			{
				Console.WriteLine(item.ProcessName);
			}
		}
		public static void StartService(string servicename)
		{
			Process [] getService = Process.GetProcesses();
			foreach(var item in getService)
			{
				item.Start(servicename.ToString());
			}
		}
		public static void StopService(string servicename)
		{
			Process [] getService = Process.GetProcesses();
			foreach(var item in getService)
			{
				item.Kill(servicename.ToString());
			}
		}
		public static void RefreshService(string servicename)
		{
			Process [] getService = Process.GetProcesses();
			foreach(var item in getService)
			{
			    item.Refresh(servicename.ToString());
			}
		}
		
		public static void Main (string[] args)
		{
		    getServiceList();
			
		
		}
	}
}

