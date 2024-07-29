import { useEffect, useRef, useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import LogoIcon from '../../images/logo/silas.svg';
import {
  LeftArrow,
} from '../svg/svg';

import { GrDashboard, GrFolder } from "react-icons/gr";
import { HiOutlineDocumentReport } from "react-icons/hi";
import { IoMdAnalytics } from "react-icons/io";
import { IoDocumentsOutline } from "react-icons/io5";
import { CgProfile } from "react-icons/cg";
import { IoIosSettings } from "react-icons/io";
import { MdOutlineContactSupport } from "react-icons/md";
import { BsSend } from "react-icons/bs";

interface SidebarProps {
  sidebarOpen: boolean;
  setSidebarOpen: (arg: boolean) => void;
}

const Sidebar = ({ sidebarOpen, setSidebarOpen }: SidebarProps) => {
  const location = useLocation();
  const { pathname } = location;

  const trigger = useRef<any>(null);
  const sidebar = useRef<any>(null);

  const storedSidebarExpanded = localStorage.getItem('sidebar-expanded');
  const [sidebarExpanded, setSidebarExpanded] = useState(
    storedSidebarExpanded === null ? false : storedSidebarExpanded === 'true',
  );

  // close on click outside
  useEffect(() => {
    const clickHandler = ({ target }: MouseEvent) => {
      if (!sidebar.current || !trigger.current) return;
      if (
        !sidebarOpen ||
        sidebar.current.contains(target) ||
        trigger.current.contains(target)
      )
        return;
      setSidebarOpen(false);
    };
    document.addEventListener('click', clickHandler);
    return () => document.removeEventListener('click', clickHandler);
  });

  // close if the esc key is pressed
  useEffect(() => {
    const keyHandler = ({ keyCode }: KeyboardEvent) => {
      if (!sidebarOpen || keyCode !== 27) return;
      setSidebarOpen(false);
    };
    document.addEventListener('keydown', keyHandler);
    return () => document.removeEventListener('keydown', keyHandler);
  });

  useEffect(() => {
    localStorage.setItem('sidebar-expanded', sidebarExpanded.toString());
    if (sidebarExpanded) {
      document.querySelector('body')?.classList.add('sidebar-expanded');
    } else {
      document.querySelector('body')?.classList.remove('sidebar-expanded');
    }
  }, [sidebarExpanded]);

  const sidebarMenuProps = [
    {
      name: 'Menu',
      links: [
        { label: 'Dashboard', icon: <GrDashboard />, linkTo: '/' },
        { label: 'Accounts', icon: <GrFolder />, linkTo: '/accounts' },
        { label: 'Engineering Report', icon: <HiOutlineDocumentReport />, linkTo: '/engineering' },
        // { label: 'Market Analysis', icon: <IoMdAnalytics />, linkTo: '/market-analysis' },
        { label: 'Submissions', icon: <BsSend />, linkTo: '/submissions' },
        { label: 'Document Viewer', icon: <IoDocumentsOutline />, linkTo: '/document-viewer' },
      ],
    },
    {
      name: 'Preferences',
      links: [
        { label: 'My Profile', icon: <CgProfile />, linkTo: '/profile' },
        { label: 'Settings', icon: <IoIosSettings />, linkTo: '/settings' },
      ],
    },
    {
      name: 'Support',
      links: [{ label: 'Help & Support', icon: <MdOutlineContactSupport />, linkTo: '/help' }],
    },
  ];


  return (
    <aside
      ref={sidebar}
      className={`absolute left-0 top-0 z-9999 flex h-screen w-72.5 flex-col overflow-y-hidden bg-black duration-300 ease-linear dark:bg-boxdark lg:static lg:translate-x-0 ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
    >
      <div className="flex items-center justify-between gap-2 px-6 py-5.5 lg:py-6.5">
        <NavLink className="w-full" to="/">
          <img src={LogoIcon} alt="Logo" />
          {/* Logo goes here */}
        </NavLink>

        <button
          ref={trigger}
          onClick={() => setSidebarOpen(!sidebarOpen)}
          aria-controls="sidebar"
          aria-expanded={sidebarOpen}
          className="block lg:hidden"
        >
          <LeftArrow />
        </button>
      </div>
      <div className="no-scrollbar flex flex-col overflow-y-auto duration-300 ease-linear">
        <nav className="py-4 px-4 lg:4 lg:px-6">
          {sidebarMenuProps.map((group) => {
            return (
              <div key={group.name}>
                <h3 className="mb-4 ml-4 text-md font-semibold text-bodydark2">
                  {group.name}
                </h3>
                <ul className="mb-6 flex flex-col gap-1.5">
                  {group.links.map((link, idx) => {
                    const navLinkClass = `group relative flex items-center gap-2.5 rounded-sm py-2 px-4 font-medium text-bodydark1 duration-300 ease-in-out hover:bg-graydark dark:hover:bg-meta-4 ${pathname.includes(link.linkTo)}`
                    return (
                      <li key={idx}>
                        <NavLink
                          to={link.linkTo}
                          className={({ isActive }) =>
                            isActive ? `${navLinkClass} bg-graydark dark:bg-meta-4` : navLinkClass
                          }
                        >
                          {link.icon}
                          {link.label}
                        </NavLink>
                      </li>
                    );
                  })}
                </ul>
              </div>
            );
          })}
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar;
