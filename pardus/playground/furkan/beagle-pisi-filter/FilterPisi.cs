//
// FilterPisi.cs: Parses pisi package files and crawls metadatas
//
// Copyright (C) 2006-2007 Furkan Duman <coderlord-at-gmail.com>

using System;
using System.IO;
using System.Xml;
using ICSharpCode.SharpZipLib.Zip;
using Beagle.Daemon;
using Beagle.Util;

[assembly: Beagle.Daemon.FilterTypes(typeof(Beagle.Filters.FilterPisi))]

namespace Beagle.Filters {

    public class FilterPisi : Beagle.Daemon.Filter 
    {
        public FilterPisi ()
        {
        }

        protected override void RegisterSupportedTypes()
        {
            AddSupportedFlavor(FilterFlavor.NewFromExtension(".pisi"));
            AddSupportedFlavor(FilterFlavor.NewFromMimeType("application/x-pisi"));
        }

        private ZipInputStream zStream;

        // Finds and locates zip entry by file name
        private ZipEntry GetEntry (string name) {
            ZipEntry zEntry;
            while ((zEntry = zStream.GetNextEntry ()) != null) {
                if (zEntry.Name == name)
                    return zEntry;
            }
            return null;
        }

        protected override void DoOpen (FileInfo info)
        {
            try {
                zStream = new ZipInputStream (Stream);
            }
            catch (Exception E) {
                Logger.Log.Error ("Unable to open pisi stream {0}: {1}!", info.FullName, E.Message);
                Error ();
                return;
            }
            // Go to metadata.xml in zip if avail.
            ZipEntry zEntry = this.GetEntry ("metadata.xml");
            if (zEntry == null) {
                Logger.Log.Error ("metadata.xml not found in pisi file {0}!", info.FullName);
                Error ();
                return;
            }
        }

        protected override void DoPullProperties ()
        {
            try {
                // Load decompressed zip stream into XML
                XmlDocument xml = new XmlDocument ();
                xml.Load (zStream);
                zStream.Close ();

                // Pull package metadatas
                XmlNode packageNode = xml.DocumentElement ["Package"];
                AddProperty (Beagle.Property.New ("dc:title", packageNode ["Name"].InnerText));
                foreach (XmlNode summary in packageNode.SelectNodes ("License"))
                    AddProperty (Beagle.Property.New ("fixme:license", summary.InnerText));
                foreach (XmlNode summary in packageNode.SelectNodes ("Summary"))
                    AddProperty (Beagle.Property.New ("fixme:summary", summary.InnerText));
                foreach (XmlNode description in packageNode.SelectNodes ("Description"))
                    AddProperty (Beagle.Property.New ("fixme:description", description.InnerText));

                // Pull source metadatas
                XmlNode sourceNode = xml.DocumentElement ["Source"];
                AddProperty (Beagle.Property.New ("fixme:homepage", sourceNode ["Homepage"].InnerText));
                AddProperty (Beagle.Property.NewKeyword ("dc:author", sourceNode ["Packager"]["Name"].InnerText));
                AddProperty (Beagle.Property.NewKeyword ("dc:mailto", sourceNode ["Packager"]["Email"].InnerText));

                Finished();
            }
            catch (Exception E) {
                Logger.Log.Error ("Unable to parse metadata.xml of pisi package: {0}!", E.Message);
                Error ();
            }
        }
    }
}
